#add settings
def add_setings(settings,new_setting):
    new_setting= tuple(i.lower() for i in new_setting)
    if new_setting[0] in settings.keys():
        return f"Setting '{new_setting[0]}' already exists! Cannot add a new setting with this name."
    else : 
        settings[new_setting[0]]= new_setting[1]
        return f"Setting '{new_setting[0]}' added with value '{new_setting[1]}' successfully!"
    
#update settings
def update_settings(settings,updated_setting):
    updated_setting=tuple(i.lower() for i in updated_setting)
    if updated_setting[0] in settings.keys():
        settings[updated_setting[0]]= updated_setting[1]
        return f"Setting '{updated_setting[0]}' updated to '{updated_setting[1]}' successfully!"
    else : 
        return f"Setting '{updated_setting[0]}' does not exist! Cannot update a non-existing setting."

#delete settings
def delete_settings(settings,setting_name):
    setting_name =setting_name.lower()
    if setting_name in settings.keys():
        del settings[setting_name]
        return f"Setting '{setting_name}' deleted successfully!"
    else :
        return f"Setting not found!"
    
#view settings
def view_settings(settings):
    output ="Current User Settings:\n"
    if not settings:
        return "No settings available."
    else:
        for key,value in settings.items():
            output += f"{key.capitalize()}: {value}\n"
        return output.strip()

test_settings={
    "theme": "dark",
}

#main function to test the code
if __name__ == "__main__":
    print(add_setings(test_settings,("deat","stan")))
    print(update_settings(test_settings,("theme","light")))
    print(delete_settings(test_settings,"deat"))
    print(view_settings(test_settings))
    
#converting a tuple to upper case
# test_tuple=("language","english")
# upper_tuple=tuple(i.upper() for i in test_tuple)
# print(upper_tuple)

