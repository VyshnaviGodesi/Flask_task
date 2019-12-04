from flask import Flask
import pyodbc

from flask import render_template


from config_test import read_db_config

n=str('select distinct top 5 ci.dv_task as chg_num,CONVERT(char(16), c.[chg_req.start_date],20) as StartDate,ci.dv_ci_item as ConfigItem,c.[change_request.short_description] as ShortDesc,c.[chg_req.dv_assigned_to],c.[chg_req.dv_approval],c.[chg_req.dv_priority],c.[chg_req.dv_risk],c.[Groups_with_DRG.DRG] from [dbo].[task_ci] ci inner join [dbo].[Change_Data] c on ci.dv_task = c."chg_req.number" where dv_ci_item like ');
n2=str("'%HYD%' and sys_updated_on > (getdate()-3) order by CONVERT(char(16), c.[chg_req.start_date],20) asc");

app = Flask(__name__)
@app.route('/')
def home():
    db_config = read_db_config()
    print('Connecting to MySQL database...')
    conn = pyodbc.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("select top 5 number,dv_category,u_cause_code,dv_impact,dv_opened_by,dv_assignment_group,dv_incident_state,dv_closed_by,sys_created_on from [dbo].[incident] where dv_assignment_group like '%Communication Service%' and sys_created_on >= DATEADD(month, DATEDIFF(month, 0, DATEADD(MONTH,-9,GETDATE())), 0) order by sys_created_on desc ")
    data = cursor.fetchall()
    for item in data:
        print(item)
    cursor.execute(n+n2)
    data2 = cursor.fetchall()
    for item in data2:
        print(item)
    return render_template('template.html', data=data,data2=data2)
app.run(host='0.0.0.0',debug=True)

#select distinct ci.dv_task as Chg_num,--c.[chg_req.start_date],CONVERT(char(16), c.[chg_req.start_date],20) as StartDate,ci.dv_ci_item as ConfigItem,c.[change_request.short_description] as Description ,c.[chg_task.number] as chg_task,c.[chg_req.dv_assigned_to] as req_by,c.[chg_req.dv_approval] as Status,c.[chg_req.dv_priority] as Priority,c.[chg_req.dv_risk] as Risk,c.[chg_req.dv_category] as Category,c.[chg_task.dv_assigned_to] as Chg_assigned_to,c.[Groups_with_DRG.DRG] as Chg_drgfrom [dbo].[task_ci] ciinner join [dbo].[Change_Data] c on ci.dv_task = c."chg_req.number"where sys_updated_on > (getdate()-3)--and dv_ci_item like '%HYD%'--and sys_updated_on > dateadd(d,-3,getdate())--order by c.[chg_req.start_date] ascorder by CONVERT(char(16), c.[chg_req.start_date],20) asc
