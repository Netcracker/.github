// eslint.config.mjs
import js from "@eslint/js";
import tseslint from "@typescript-eslint/eslint-plugin";
import tsParser from "@typescript-eslint/parser";
import json from "@eslint/json";

export default [
  {
    ignores: [
      "dist/**",
    ]
  },

  js.configs.recommended,

  {
    files: ["**/*.ts", "**/*.tsx"],
    languageOptions: {
      parser: tsParser,
    },
    plugins: {
      "@typescript-eslint": tseslint,
    },
    rules: {
      "no-undef": "warn",
      "n/no-missing-import": "warn",
    },
  },

  {
    files: ["**/*.json"],
    ignores: ["**/*.jsonc", "**/*.json5"],
    plugins: { json },
    language: "json/json",
    extends: ["json/recommended"],
  },
];