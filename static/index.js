

const changeToRom = document.getElementById('toRomButton');
changeToRom.addEventListener('click',  async () => {
    const inputToRom = document.getElementById('toRomInput');
    const result = await fetch(`http://localhost:5000/ator?arab=${inputToRom.value}`) 
    const json = await result.json();
    const paraToRom = document.getElementById('toRomText');
    paraToRom.textContent +=`${inputToRom.value} converts to Roman numeral is ${json.roman_numeral}`;
    inputToRom.value = ''
});




const changeToArabic = document.getElementById('toArabicButton');
changeToArabic.addEventListener('click', async() => {
    const inputToArabic = document.getElementById("toArabicInput");
    const result = await fetch(`http://localhost:5000/rtoa?rom=${inputToArabic.value}`)
    const json = await result.json();
    const paraToRom = document.getElementById('toArabicText');
    paraToRom.textContent += `${inputToArabic.value} converts to Arabic number is ${json.Arabic_number}`; 
    inputToArabic.value = ''
});                                 