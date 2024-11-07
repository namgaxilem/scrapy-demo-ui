function restoreCookiesAndLCStorage(data) {
    let lc_data = data
    Object.keys(lc_data).forEach(function (key) {
        window.localStorage.setItem(key, lc_data[key])
    })
}
restoreCookiesAndLCStorage(data_tobe_replace)
