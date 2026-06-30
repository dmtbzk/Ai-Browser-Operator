import { IconButton } from "@chakra-ui/react";
import { useTheme } from "next-themes";
import { LuSun, LuMoon } from "react-icons/lu";

export function ColorModeToggle() {
  const { resolvedTheme, setTheme } = useTheme();
  const isDark = resolvedTheme === "dark";

  return (
    <IconButton
      aria-label="Tema değiştir"
      variant="ghost"
      size="sm"
      onClick={() => setTheme(isDark ? "light" : "dark")}
    >
      {isDark ? <LuSun /> : <LuMoon />}
    </IconButton>
  );
}
