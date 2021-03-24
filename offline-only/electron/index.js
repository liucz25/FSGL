const { app, BrowserWindow } = require('electron')
const path = require('path')

function creatWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    })
    win.loadFile("index.html")

}

app.whenReady().then(() => {
    creatWindow()
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows.length === 0) {
            creatWindow()
        }
    })
})


app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})