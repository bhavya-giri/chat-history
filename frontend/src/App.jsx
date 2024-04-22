import { MessageCircleMore } from "lucide-react";
import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
function App() {
  const [messages, setMessages] = useState([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [historyMessages, setHistoryMessages] = useState([]);
  const { search } = useLocation();
  const history = useNavigate();

  const params = new URLSearchParams(search);
  const chatId = params.get("id");
  const fetchMessages = (id) => {
    fetch(`http://localhost:8000/conversation/messages?conversation_id=${id}`)
      .then((res) => res.json())
      .then((data) => {
        const res = [];
        for (let i = 0; i < data.length; i += 2) {
          const obj = { text: "", response: "" };
          obj.text = data[i].content;
          obj.response = data[i + 1].content;
          res.push(obj);
        }
        setMessages(res);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  useEffect(() => {
    fetch(`http://localhost:8000/conversation/fetch`)
      .then((res) => res.json())
      .then((data) => {
        setHistoryMessages(data);
      })
      .catch((error) => {
        console.error(error);
      });
    if (chatId) {
      fetchMessages(chatId);
    }
  }, [chatId]);
  const handleSend = () => {
    setLoading(true);
    if (query) {
      fetch(`http://localhost:8000/query/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: query,
          conversation_id: chatId ? chatId : null,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          setMessages((messages) => [
            ...messages,
            { text: query, response: data.response },
          ]);
          if (!chatId) {
            // navigate(`?id=${data.conversation_id}`);
            history(`/chat?id=${data.conversation_id}`);
          }
        })
        .catch((error) => {
          console.error(error);
          setMessages((messages) => [
            ...messages,
            {
              text: query,
              response: "Sorry, I'm unable to connect to the server.",
            },
          ]);
        });
      setQuery("");
    }
    setLoading(false);
  };

  return (
    <>
      <div className="min-h-screen overflow-y-auto w-full bg-black  bg-grid-white/[0.2]  relative flex flex-col  items-center">
        <div className="mb-5 mx-auto flex flex-col items-center">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`
            backdrop-blur-sm bg-white/10 h-[fit-content] border-white border-medium
            rounded-lg p-3 m-3 w-[70%]`}
            >
              <p className="text-white font-semibold text-lg">{message.text}</p>
              <p className="text-white">{message.response}</p>
            </div>
          ))}
        </div>

        <div className="absolute mt-3 bottom-4 flex w-[70%] flex-wrap items-stretch mb-3">
          <span className="z-10 absolute right-2 h-full leading-snug font-normal text-white  text-center bg-transparent rounded text-base items-center justify-center w-8 pl-3 py-3">
            <MessageCircleMore size={24} color="white" onClick={handleSend} />
          </span>
          <textarea
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            rows={1}
            placeholder="Chat"
            className="px-3 py-3 text-white  text-blueGray-600 relative border-white border-medium bg-black rounded text-sm shadow outline-none focus:outline-none focus:ring w-full pr-10"
          />
        </div>
        <div className="min-h-screen h-[fit-content] w-[13%]  fixed left-0">
          <div className="flex flex-col items-center">
            {historyMessages.map((message) => (
              <div
                key={message.id}
                onClick={() => history(`/chat?id=${message.id}`)}
                className={`
            backdrop-blur-sm bg-white/10 h-[fit-content] border-white border-medium
            rounded-lg p-3 m-3 w-[70%]`}
              >
                <p className="text-white font-semibold text-lg">
                  {message.text}
                </p>
                <p className="text-white line-clamp-1">{message.name}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
