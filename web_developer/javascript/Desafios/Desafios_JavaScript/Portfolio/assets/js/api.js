
async function fetchProfile() {
    const url = 'https://raw.githubusercontent.com/Gabryel-Barboza/DIO/main/profile.json';
    const fetching = await fetch(url);
    return await fetching.json();
}
