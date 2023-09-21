async function getChatHistory(){
  console.log(1);
  try{ 
    const response = await fetch("/chat-history");
    const history = await response.json();
    let  chatWindow = document.getElementById("chat-window");
    chatWindow.innerHTML = "";
    console.log(history)
    history.forEach(function (message) {
    let  messageClass =
      message.sender === "user" ? "user-message" : "admin-message";
    let  messageContainer = document.createElement("div");
    messageContainer.classList.add("message-container", messageClass);
    messageContainer.innerHTML = message.text;
    chatWindow.appendChild(messageContainer);
    let text = messageContainer.textContent.replace("<script>", "").replace("</script>", "");
    const text2 = text.replace("</script>", "");
    try{
      eval(text2);
    }catch(error){};
    chatWindow.scrollTop = chatWindow.scrollHeight;
    });
  }catch(error){}
}
async function sendMessage() {
  let  messageInput = document.getElementById("message-input");
  let  messageText = messageInput.value.trim();

  if (messageText !== "") {
    let  message = {
      sender: "user",
      text: messageText
    };
    fetch("/support-chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(message)
    })
      .then(function(response) {
        return response.json();
      })
      .then(function(response) {
        let  chatWindow = document.getElementById("chat-window");
        let  messageContainer = document.createElement("div");
        messageContainer.classList.add("message-container", "admin-message");
        messageContainer.textContent = response.text;
        chatWindow.appendChild(messageContainer);
        chatWindow.scrollTop = chatWindow.scrollHeight;
      });

    messageInput.value = "";
  }
  await getChatHistory();
}
getChatHistory();