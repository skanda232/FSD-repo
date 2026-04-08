interface Book{
    readonly title: string;
    author: string;
    
    year: number;
}

let automaticHabits: Book = {
    title: "Atomic Habits",
    author: "Kishimoto",
    year: 2024

}

let newBook: Book[] = [
    {title: "Angels and Demons", author: "Dan Brown", year: 2000},
    {title: "The Da Vinci Code", author: "Dan Brown", year: 2003},
    {title: "Inferno", author: "Dan Brown", year: 2013}
]






export { automaticHabits, newBook }
