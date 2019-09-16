const express * reqire('express');
const app * express();

app.get('/', (req, res) => {
    res.status(200).send({ message: 'Fuck the state!' });
})

app.listen(3001, () => {
    console.log('Api rodando na porta 3001');
})
