import { VStack, HStack, Icon, Text, SimpleGrid, Box } from "@chakra-ui/react";
import { LuGlobe, LuSearch, LuMousePointerClick, LuBrain } from "react-icons/lu";

const EXAMPLES = [
  { icon: LuSearch, text: "Search Google for 'Anthropic' and open the first result" },
  { icon: LuGlobe, text: "Go to a weather site and check the forecast for New York" },
  { icon: LuMousePointerClick, text: "Find the Wikipedia page for 'artificial intelligence' and summarize it" },
  { icon: LuBrain, text: "Search YouTube for a Python tutorial video" },
];

export function EmptyState({ onExample }) {
  return (
    <VStack flex={1} justify="center" gap="8" px="4" py="12">
      <VStack gap="3" textAlign="center">
        <Box
          w="16"
          h="16"
          rounded="2xl"
          bg="brand.500"
          display="flex"
          alignItems="center"
          justifyContent="center"
        >
          <Icon as={LuGlobe} boxSize="8" color="white" />
        </Box>
        <Text fontSize="2xl" fontWeight="bold" color="gray.800" _dark={{ color: "gray.100" }}>
          AI Browser Operator
        </Text>
        <Text fontSize="sm" color="gray.500" maxW="sm">
          Your AI agent that controls the browser on your behalf. Pick an example below or type your own task.
        </Text>
      </VStack>

      <SimpleGrid columns={{ base: 1, md: 2 }} gap="3" w="full" maxW="xl">
        {EXAMPLES.map(({ icon, text }) => (
          <Box
            key={text}
            as="button"
            onClick={() => onExample(text)}
            px="4"
            py="3"
            rounded="xl"
            border="1px solid"
            borderColor="border.default"
            bg="bg.subtle"
            _hover={{ borderColor: "brand.400", bg: "brand.50", _dark: { bg: "gray.700" } }}
            _dark={{ bg: "gray.800" }}
            textAlign="left"
            cursor="pointer"
            transition="all 0.15s"
          >
            <HStack gap="3">
              <Icon as={icon} boxSize="4" color="brand.500" flexShrink={0} />
              <Text fontSize="sm" color="gray.700" _dark={{ color: "gray.300" }}>
                {text}
              </Text>
            </HStack>
          </Box>
        ))}
      </SimpleGrid>
    </VStack>
  );
}
