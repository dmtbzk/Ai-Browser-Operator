import { VStack, Text, Box, Icon, HStack, IconButton } from "@chakra-ui/react";
import { LuGlobe, LuPlus, LuTrash2 } from "react-icons/lu";

export function Sidebar({ onClear }) {
  return (
    <Box
      w="64"
      flexShrink={0}
      borderRight="1px solid"
      borderColor="border.default"
      bg="bg.subtle"
      display="flex"
      flexDir="column"
      h="full"
    >
      {/* Logo */}
      <HStack gap="3" px="4" py="5" borderBottom="1px solid" borderColor="border.default">
        <Box
          w="8"
          h="8"
          rounded="lg"
          bg="brand.500"
          display="flex"
          alignItems="center"
          justifyContent="center"
          flexShrink={0}
        >
          <Icon as={LuGlobe} boxSize="4" color="white" />
        </Box>
        <VStack gap="0" align="flex-start">
          <Text fontSize="sm" fontWeight="bold" lineHeight="tight" color="gray.800" _dark={{ color: "gray.100" }}>
            AI Browser
          </Text>
          <Text fontSize="xs" color="gray.500">
            Operator
          </Text>
        </VStack>
      </HStack>

      {/* New Chat */}
      <Box px="3" py="3">
        <Box
          as="button"
          onClick={onClear}
          w="full"
          px="3"
          py="2"
          rounded="lg"
          border="1px dashed"
          borderColor="border.default"
          _hover={{ borderColor: "brand.400", bg: "brand.50", _dark: { bg: "gray.700" } }}
          cursor="pointer"
          transition="all 0.15s"
        >
          <HStack gap="2" justify="center">
            <Icon as={LuPlus} boxSize="4" color="gray.500" />
            <Text fontSize="sm" color="gray.500">
              Yeni Sohbet
            </Text>
          </HStack>
        </Box>
      </Box>

      <Box flex={1} />

      {/* Footer */}
      <Box px="4" py="4" borderTop="1px solid" borderColor="border.default">
        <HStack justify="space-between">
          <Text fontSize="xs" color="gray.400">
            v0.1.0
          </Text>
          <IconButton
            aria-label="Sohbeti temizle"
            variant="ghost"
            size="xs"
            colorPalette="red"
            onClick={onClear}
          >
            <LuTrash2 />
          </IconButton>
        </HStack>
      </Box>
    </Box>
  );
}
