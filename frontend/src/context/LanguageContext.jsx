import { createContext, useContext, useState } from "react";

import en from "../translations/en";
import hi from "../translations/hi";
import gu from "../translations/gu";

const LanguageContext = createContext();

const languages = {
  en,
  hi,
  gu,
};

export const LanguageProvider = ({ children }) => {
  const [language, setLanguage] = useState("en");

  return (
    <LanguageContext.Provider
      value={{
        language,
        setLanguage,
        t: languages[language],
      }}
    >
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = () =>
  useContext(LanguageContext);