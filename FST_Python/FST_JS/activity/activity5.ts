interface Settings{
    theme? :"light" | "dark";
    fontSize? : number;

}

let appSettings = (settings: Settings) =>  {
    const theme = settings.theme || "light";
    const fontSize = settings.fontSize ?? 14;

    console.log(`Theme: ${theme}`);
    console.log(`Font Size: ${fontSize}`);
}

export { appSettings };