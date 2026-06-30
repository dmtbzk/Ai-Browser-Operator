import { useCallback, useRef, useState } from "react";
import { HStack, Textarea, IconButton, Box } from "@chakra-ui/react";
import { LuSend, LuSquare } from "react-icons/lu";

export function ChatInput({ onSubmit, disabled }) {
  const [value, setValue] = useState("");
  const textareaRef = useRef(null);

  const handleSubmit = useCallback(() => {
    const trimmed = value.trim();
    if (!trimmed || disabled) return;
    onSubmit(trimmed);
    setValue("");
    textareaRef.current?.focus();
  }, [value, disabled, onSubmit]);

  const handleKeyDown = useCallback(
    (e) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        handleSubmit();
      }
    },
    [handleSubmit]
  );

  return (
    <Box
      px="4"
      py="3"
      borderTop="1px solid"
      borderColor="border.default"
      bg="bg.surface"
    >
      <HStack gap="3" maxW="3xl" mx="auto" align="flex-end">
        <Textarea
          ref={textareaRef}
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type a task… (Shift+Enter for new line)"
          resize="none"
          rows={1}
          minH="10"
          maxH="36"
          overflowY="auto"
          fontSize="sm"
          borderRadius="xl"
          borderColor="border.default"
          _focus={{ borderColor: "brand.500", boxShadow: "0 0 0 1px var(--chakra-colors-brand-500)" }}
          flex={1}
          disabled={disabled}
          css={{ fieldSizing: "content" }}
        />
        <IconButton
          aria-label="Send"
          onClick={handleSubmit}
          disabled={!value.trim() || disabled}
          colorPalette="blue"
          rounded="xl"
          size="md"
        >
          {disabled ? <LuSquare /> : <LuSend />}
        </IconButton>
      </HStack>
    </Box>
  );
}
