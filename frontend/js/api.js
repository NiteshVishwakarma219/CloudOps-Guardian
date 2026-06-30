const BASE_URL = "http://13.201.132.138:8000";

async function fetchData(endpoint) {
    try {
        const response = await fetch(`${BASE_URL}${endpoint}`);

        if (!response.ok) {
            throw new Error("API Error");
        }

        return await response.json();

    } catch (error) {
        showToast("⚠️ Failed to load data from server");
        console.error(error);

        return {
            error: true
        };
    }
}