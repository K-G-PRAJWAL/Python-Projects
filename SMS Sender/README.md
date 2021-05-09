This is SMS sender project using Fast2SMS in Python. The main purpose of this project is to send sms efficiently using Python promptly to any number of your choice with the user specified text message

Instructions on how code is implemented:

Import the required libraries
To send sms we need an API. Here we use a Fast2SMS API as gateway for successful transmission of messages.
We provide the respective url of Fast2SMS and parameters like authorization, sender_id, route, language in the declaration. You can get all these details from Fast2SMS.
To acquire these details, you have to sign up in FastSms. Then go to Dev API and select the API key Tab and click generate. The API key is generated successfully
Now come to Dev API tab, you can see the syntax of how parameters can be declared. To know the declaration of parameters, you can refer to Fast2SMS API Documentation.
You can head to Quick SMS API. And further into POST method, as this method is secure for messages sending.
Here the parameter details are given to ensure the flow of messages. It can be declared in a code. As you can see in a code, that I haven't mentioned number or message for flexibility.
Responses are directed to the JSON file.
Define a button to get a message to check if message is sent or not using btn_clk function
I have now created GUI interface with labels, extnumber and textmessages with the required specifications. I have also declared the send and quit button for operations and directed it to btn_clk.
I have also placed a SMS logo to appear on GUI. Make sure the file is in this folder.
