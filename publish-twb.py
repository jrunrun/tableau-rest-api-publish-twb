import tableauserverclient as TSC

def ts_signin(ts_username, ts_password, ts_site_name, ts_url):
    
    tableau_auth = TSC.TableauAuth(ts_username, ts_password, site_id=ts_site_name)
    server = TSC.Server(ts_url, use_server_version=True)
    # overwrite_true = TSC.Server.PublishMode.Overwrite

    server.auth.sign_in(tableau_auth)
    return server
    
def ts_find_project(server, destination_project_name):
    # Step 2: Get all the projects on server, then look for destination_project_name.
    # all_projects, pagination_item = server.projects.get()
    # destination_project = next((project for project in all_projects if project.name == destination_project_name), None)

    # return destination_project[0]

    all_projects, pagination_item = server.projects.get()

    # matching_project = next((project for project in all_projects if project.name == destination_project_name), None)
    # print(matching_project)
    # print(type(matching_project))

    # print(all_projects[1].name)
    # print(all_projects[1].id)
    #
    #
    for project in all_projects:
       
        if project.name == destination_project_name:
            print("found matching project")
            print(project.name)
            print(project.id)
            matching_project = project

    return matching_project

def ts_publish_twb(server, destination_project, twb_file_name):
    
    print(destination_project.name)
    print(destination_project.id)
    print(destination_project.is_default())
    wb_item = TSC.WorkbookItem(project_id=destination_project.id)


  

   
    print(twb_file_name)
    wb_item = server.workbooks.publish(wb_item, twb_file_name, 'Overwrite')

    return wb_item


ts_username = ''
ts_password = ''
ts_site_name = ''
ts_url = '' 
destination_project_name = ''
twb_file_name = ''


server = ts_signin(ts_username, ts_password, ts_site_name, ts_url)
destination_project = ts_find_project(server, destination_project_name)
wb = ts_publish_twb(server, destination_project, twb_file_name)