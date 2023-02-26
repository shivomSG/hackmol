const express = require('express')

const bodyParser = require('body-parser')

const path = require('path')

const PUBLISHABLE_KEY = "pk_test_51MfLRPSDw4pNhHCO5YJaD2MRVmnFNzNFew2vL05X0IuOTljjKm0ywauTgpKPU6AHK06LY5NRQmbu0pIlVwxektG100CqWMoxPH"

const SECRET_KEY ="sk_test_51MfLRPSDw4pNhHCOT1GQm6t99NDG15TOYKqZtF3be9IkrrGRgZ1cTDFsrcictqDkR1SnbunPYnYqKjiuDPAlkVFx009FLTJGNC"

const stripe = require('stripe')(SECRET_KEY)

const app = express()


app.use(bodyParser.urlencoded({extended:false}))
app.use(bodyParser.json())

app.set("view engine","ejs")

const PORT = process.env.PORT || 3000

app.get('/',(req,res) => {
    res.render('Ghar',{
        key:PUBLISHABLE_KEY
        

    })
})

app.post('/payment',(req,res) => {
    stripe.customers.create({
        email:req.body.stripeEmail,
        source:req.body.stripeToken,
        address:{
            line1:'12 Mountain Valley New Delhi',
            postal_code:'110092',
            city:'New Delhi',
            state:'Delhi'
        }
    })
    .then((customer) => {
        return stripe.charges.create({
            amount:7000,
            description:'BOOK',
            currency:'USD',
            customer:customer.id
        })
    })
    .then((charge) =>{
        console.log(charge)
        res.render('success')
    })
})


app.listen(PORT,() => {
    console.log(`App is listening on ${PORT}`)
})