import { Box, HStack } from "@chakra-ui/react";
import { Sidebar } from "./components/Sidebar";
import { ChatWindow } from "./components/ChatWindow";
import { useChat } from "./hooks/useChat";

function App() {
  const { messages, loading, error, submit, clear } = useChat();

  return (
    <HStack h="100dvh" gap="0" bg="bg.surface" overflow="hidden">
      <Sidebar onClear={clear} />
      <Box flex={1} h="full" overflow="hidden">
        <ChatWindow
          messages={messages}
          loading={loading}
          error={error}
          onSubmit={submit}
          onExample={submit}
        />
      </Box>
    </HStack>
  );
}

export default App;
