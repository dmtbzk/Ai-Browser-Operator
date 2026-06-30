import { HStack, Box, Icon } from "@chakra-ui/react";
import { LuBot } from "react-icons/lu";
import { keyframes } from "@emotion/react";

const bounce = keyframes`
  0%, 80%, 100% { transform: translateY(0); opacity: 0.4; }
  40%            { transform: translateY(-6px); opacity: 1; }
`;

function Dot({ delay }) {
  return (
    <Box
      w="2"
      h="2"
      rounded="full"
      bg="gray.400"
      _dark={{ bg: "gray.500" }}
      animation={`${bounce} 1.2s ease-in-out ${delay}s infinite`}
    />
  );
}

export function TypingIndicator() {
  return (
    <HStack align="flex-start" gap="3" alignSelf="flex-start">
      <Box
        flexShrink={0}
        w="8"
        h="8"
        rounded="full"
        display="flex"
        alignItems="center"
        justifyContent="center"
        bg="gray.100"
        _dark={{ bg: "gray.700" }}
      >
        <Icon as={LuBot} boxSize="4" color="gray.600" _dark={{ color: "gray.300" }} />
      </Box>
      <Box
        px="4"
        py="3"
        rounded="2xl"
        roundedTopLeft="sm"
        bg="bg.muted"
        _dark={{ bg: "gray.700" }}
        shadow="sm"
      >
        <HStack gap="1">
          <Dot delay={0} />
          <Dot delay={0.2} />
          <Dot delay={0.4} />
        </HStack>
      </Box>
    </HStack>
  );
}
