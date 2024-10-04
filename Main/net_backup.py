from netmiko import ConnectHandler

connection = ConnectHandler(device_type="cisco_ios", host="192.168.1.2", username="cisco", password="12345", port="22", secret="12345")

connection.enable()

output = connection.send_command("sh run")

text_file = open("Output.txt", "w")
text_file.write(output)
text_file.close()