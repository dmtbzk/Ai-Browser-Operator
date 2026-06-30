import { useCallback, useReducer } from "react";
import { sendMessage } from "../services/api";

const initialState = {
  messages: [],
  loading: false,
  error: null,
};

function reducer(state, action) {
  switch (action.type) {
    case "SEND":
      return {
        ...state,
        loading: true,
        error: null,
        messages: [
          ...state.messages,
          { id: action.id, role: "user", content: action.content, ts: Date.now() },
        ],
      };
    case "RECEIVE":
      return {
        ...state,
        loading: false,
        messages: [
          ...state.messages,
          { id: action.id, role: "assistant", content: action.content, ts: Date.now() },
        ],
      };
    case "ERROR":
      return { ...state, loading: false, error: action.error };
    case "CLEAR":
      return initialState;
    default:
      return state;
  }
}

export function useChat() {
  const [state, dispatch] = useReducer(reducer, initialState);

  const submit = useCallback(async (text) => {
    const userMsgId = crypto.randomUUID();
    dispatch({ type: "SEND", id: userMsgId, content: text });

    try {
      const answer = await sendMessage(text);
      dispatch({ type: "RECEIVE", id: crypto.randomUUID(), content: answer });
    } catch (err) {
      dispatch({
        type: "ERROR",
        error: err?.response?.data?.detail ?? err.message ?? "An unexpected error occurred.",
      });
    }
  }, []);

  const clear = useCallback(() => dispatch({ type: "CLEAR" }), []);

  return { ...state, submit, clear };
}
