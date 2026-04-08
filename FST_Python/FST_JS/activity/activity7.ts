type userResponse = {
    id: number;
    name: string;
    email: string;
    
}
async function fetchUserData(userId: number): Promise<userResponse> {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (userId == 1) {
                if(userId == 1){
                    resolve({
                        id: 1,
                        name: "Skanda",
                        email: "skanda@example.com"
                    });
                } else {
                    reject(new Error("User not found"));
                }
            }
        }, 2000);
    });
}


// run a demo
async function demo() {
    try {
        const userData = await fetchUserData(1);
        console.log("User Data:", userData);}
        catch (error) { 
            console.error("Error fetching user data:", error);
        }
}
export {demo};