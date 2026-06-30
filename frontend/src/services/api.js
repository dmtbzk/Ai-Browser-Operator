import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

const client = axios.create({
  baseURL: BASE_URL,
  headers: { "Content-Type": "application/json" },
  timeout: 120_000,
});

export async function sendMessage(message) {
  const { data } = await client.post("/chat", { message });
  return data.answer;
}
