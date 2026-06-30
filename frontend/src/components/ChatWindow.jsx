import { useEffect, useRef } from "react";
import { Box, VStack, Alert } from "@chakra-ui/react";
import { MessageBubble } from "./MessageBubble";
import { TypingIndicator } from "./TypingIndicator";
import { EmptyState } from "./EmptyState";
import { ChatInput } from "./ChatInput";

export function ChatWindow({ messages, loading, error, onSubmit, onExample }) {
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const isEmpty = messages.length === 0 && !loading;

  return (
    <Box display="flex" flexDir="column" h="full" overflow="hidden">
      <Box flex={1} overflowY="auto" py="6">
        {isEmpty ? (
          <EmptyState onExample={onExample} />
        ) : (
          <VStack gap="4" align="stretch" maxW="3xl" mx="auto" px="4">
            {messages.map((msg) => (
              <MessageBubble key={msg.id} message={msg} />
            ))}
            {loading && <TypingIndicator />}
            {error && (
              <Alert.Root status="error" rounded="xl">
                <Alert.Indicator />
                <Alert.Description fontSize="sm">{error}</Alert.Description>
              </Alert.Root>
            )}
            <Box ref={bottomRef} />
          </VStack>
        )}
      </Box>

      <ChatInput onSubmit={onSubmit} disabled={loading} />
    </Box>
  );
}
