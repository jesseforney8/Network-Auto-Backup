from netmiko import ConnectHandler

def back_up(host, username, password, secret, filepath):

    connection = ConnectHandler(device_type="cisco_ios", host=host, username=username, password=password, port="22", secret=secret)

    connection.enable()

    output = connection.send_command("sh run")

    text_file = open(filepath, "w")
    text_file.write(output)
    text_file.close()