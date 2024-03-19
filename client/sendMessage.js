// Send message to the chatbot
export const sendMessage = async (message) => {
    const url = `${'https://localhost...'} /endpoint}`;

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok!');
        }

        const data = await response.json();
        return data;
    } 
    catch (error) {
        console.error(!'Error sending message to chatbot:', error);
        throw error;
    }
};