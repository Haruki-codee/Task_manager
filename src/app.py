from flask import Flask,g,jsonify,render_template,request
import sqlite3
import datetime
app = Flask(__name__)

database = "Task.db"

def get_db():
    db=getattr(g,'_database',None)
    if db is None:
        db = g._database = sqlite3.connect(database)
        db.row_factory = sqlite3.Row
    return db
def init_db():
    with app.app_context():
        db=get_db()
        with app.open_resource('schema.sql',mode='r') as f:
            db.cursor().executescript(f.read())

        db.commit()
@app.before_request
def before_request():
    g._database = get_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/Post",methods=["Post"])
def add_taask():
    data = request.get_json()
    if not data or not data.get("task"):
        return jsonify({"error":"text is requried"}),400
    task_text = data.get("task")
    status = data.get("status","Pending").title()
    date_val = data.get("dates", datetime.date.today().isoformat())  
    db = get_db()
    if status in ("Pending", "In Progress", "Done"):
        db.execute("Insert into task_manager (task,status,dates) values (?,?,?)",(task_text,status,date_val))
        db.commit()
        return jsonify({
            "message": "Task added successfully",
            "task": task_text,
            "status": status,
            "date": date_val
        }), 201
    else:
        return jsonify({"message":"status only take progess,pending,complete nothing else"}),400
@app.route("/Get",methods=["GET"])
def read():
    db =get_db()
    task_id = request.args.get("id")
    if task_id:
        row = get_db().execute("select * from task_manager where id=?",(task_id,)).fetchall()
    else:
        row = db.execute("SELECT * FROM task_manager").fetchall()  
    return jsonify([ dict(r) for r in row]),200
@app.route("/update/<int:task_id>",methods=["PUT"])
def update(task_id):
    data = request.get_json()
    if not data or not data.get("status"):
        return jsonify({"error":"need data"}),400
    new_status = data.get("status").title()
    db = get_db()
    if new_status in ("Pending", "In Progress", "Done"):
        cur = db.execute("UPDATE task_manager SET status = ? WHERE id = ?",(new_status,task_id))
        db.commit()
        counts = cur.rowcount
        if cur.rowcount>0:
            return jsonify({"message":"done","rows":counts}),200
        else:
            return jsonify({"message":"Nothing update"}),404
    else:
        return jsonify({"message":"status only take progess,pending,complete nothing else"}),400
@app.route('/Delete/<int:task_id>',methods=["Delete"])
def delete(task_id):
    db= get_db()
    cur = db.execute("DELETE FROM task_manager WHERE id = ?", (task_id,))
    db.commit()
    if cur.rowcount == 0:
        return jsonify({"message":"Any Record did not delete"}),404
    else:
        return jsonify({"message":"data is deleted"}),200
    


if __name__=="__main__":
    init_db()
    app.run(debug=True)