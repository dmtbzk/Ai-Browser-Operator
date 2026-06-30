import { createSystem, defaultConfig, defineConfig } from "@chakra-ui/react";

const config = defineConfig({
  theme: {
    tokens: {
      colors: {
        brand: {
          50: { value: "#eff6ff" },
          100: { value: "#dbeafe" },
          200: { value: "#bfdbfe" },
          300: { value: "#93c5fd" },
          400: { value: "#60a5fa" },
          500: { value: "#3b82f6" },
          600: { value: "#2563eb" },
          700: { value: "#1d4ed8" },
          800: { value: "#1e40af" },
          900: { value: "#1e3a8a" },
        },
      },
      fonts: {
        heading: { value: "'Inter', sans-serif" },
        body: { value: "'Inter', sans-serif" },
        mono: { value: "'JetBrains Mono', 'Fira Code', monospace" },
      },
    },
    semanticTokens: {
      colors: {
        "bg.surface": {
          value: { base: "#ffffff", _dark: "#0f172a" },
        },
        "bg.subtle": {
          value: { base: "#f8fafc", _dark: "#1e293b" },
        },
        "bg.muted": {
          value: { base: "#f1f5f9", _dark: "#334155" },
        },
        "border.default": {
          value: { base: "#e2e8f0", _dark: "#334155" },
        },
      },
    },
  },
});

export const system = createSystem(defaultConfig, config);
