function fetchData(callback) {
    setTimeout(() => {
        const data = 'Veri';
        callback(data);
    }, 1000);
}

fetchData((data) => {
    console.log('Veri alındı:', data); //burda callback ile veri alındığında yazdırıyoruz
});
