const BASE_URL = "http://13.201.132.138:8000";

async function fetchData(endpoint) {
    try {
        const response = await fetch(`${BASE_URL}${endpoint}`);

        console.log("STATUS:", response.status);

        const data = await response.json();
        console.log("API DATA:", data);

        return data;

    } catch (error) {
        console.error("FETCH ERROR:", error);

        return {
            error: true
        };
    }
}