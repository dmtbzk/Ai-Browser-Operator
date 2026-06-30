import { Box, Text, HStack, Icon } from "@chakra-ui/react";
import { LuBot, LuUser } from "react-icons/lu";

function Avatar({ role }) {
  const isUser = role === "user";
  return (
    <Box
      flexShrink={0}
      w="8"
      h="8"
      rounded="full"
      display="flex"
      alignItems="center"
      justifyContent="center"
      bg={isUser ? "brand.500" : "gray.100"}
      _dark={{ bg: isUser ? "brand.600" : "gray.700" }}
    >
      <Icon
        as={isUser ? LuUser : LuBot}
        boxSize="4"
        color={isUser ? "white" : "gray.600"}
        _dark={{ color: isUser ? "white" : "gray.300" }}
      />
    </Box>
  );
}

export function MessageBubble({ message }) {
  const isUser = message.role === "user";

  return (
    <HStack
      align="flex-start"
      gap="3"
      flexDir={isUser ? "row-reverse" : "row"}
      maxW="80%"
      alignSelf={isUser ? "flex-end" : "flex-start"}
    >
      <Avatar role={message.role} />
      <Box
        px="4"
        py="3"
        rounded="2xl"
        roundedTopRight={isUser ? "sm" : "2xl"}
        roundedTopLeft={isUser ? "2xl" : "sm"}
        bg={isUser ? "brand.500" : "bg.muted"}
        _dark={{ bg: isUser ? "brand.600" : "gray.700" }}
        shadow="sm"
        maxW="full"
      >
        <Text
          fontSize="sm"
          color={isUser ? "white" : "gray.800"}
          _dark={{ color: isUser ? "white" : "gray.100" }}
          whiteSpace="pre-wrap"
          lineHeight="tall"
        >
          {message.content}
        </Text>
      </Box>
    </HStack>
  );
}
