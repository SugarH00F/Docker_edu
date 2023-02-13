import fs from 'fs'

fs.appendFile('mw-file.txt','Файл создан Node.js', (err) => {
    if (err) throw err
    console.log ('Файл сохранен!')
})