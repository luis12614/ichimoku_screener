# Ichimoku Screener

This code is a daily stock screener goes through all NYSE, NASDAQ and AMEX stocks and calculates their ichimoku values to determine if an important price event has occured. It gathers the stock tickers and automatically sends an email to everyone on the [email list.](https://docs.google.com/spreadsheets/d/1yJkEd5u12niaFBPlglZO63iM4nSf-SYaXaBFhVCWX8Q/edit#gid=0)

# Ichimoku Screener
Este código es un filtro de acciones diario que escribí que pasa por todas las acciones de NYSE, NASDAQ y AMEX y calcula sus valores de ichimoku para determinar si ha ocurrido un evento de precio importante. Reúne los tickers de acciones y envía automáticamente un correo electrónico a todos en la lista de correo electrónico.

### Sample Email ## Ejemplo del Email

![alt text](https://github.com/luis12614/ichimoku_screener/blob/main/images/SampleIchimokuEmail.png "Sample Email")

### What is Ichimoku?

The Ichimoku Cloud is a technical indicator used most commonly on financial securities to better understand current and future price action. The cloud is particularly useful because it has two leading spans that are plotted 26 periods ahead on the chart. These spans give an indication of the trend future prices may take, which when combined with other technical analysis tools, can be used to trade more profitably.

## ¿Qué es Ichimoku?
La nube Ichimoku es un indicador técnico que se usa con mayor frecuencia en valores financieros para comprender mejor la acción del precio actual y futura. La nube es particularmente útil porque tiene dos intervalos principales que se trazan 26 períodos adelante en el gráfico. Estos intervalos dan una indicación de la tendencia que pueden tomar los precios futuros, que cuando se combinan con otras herramientas de análisis técnico, se pueden utilizar para comerciar de manera más rentable.


[StockCharts explanation](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:ichimoku_cloud)

### What does this screener look for?

My screener (which is still a work in progress) looks for Tenkan-sen/Kijun-sen (TK) crosses, bullish cloud folds (span A overtakes span B) and price action that leaves the cloud in a bullish manner. It filters stocks based on volume, marketcap and PE ratio, as well as stocks under $1.00 (no pennystocks).

## ¿Qué busca este evaluador?
Mi evaluador (que todavía es un trabajo en progreso) busca cruces Tenkan-sen / Kijun-sen (TK), pliegues de nubes alcistas (el tramo A supera al tramo B) y la acción del precio que abandona la nube de manera alcista. Filtra las acciones según el volumen, la capitalización de mercado y la relación PE, así como las acciones por debajo de $ 1,00 (sin centavos).


### How do I get on the email list?

Add your name in the A column of the [Google Sheet.](https://docs.google.com/spreadsheets/d/1yJkEd5u12niaFBPlglZO63iM4nSf-SYaXaBFhVCWX8Q/edit#gid=0)

## ¿Cómo me inscribo en la lista de correo electrónico?
Agregue su nombre en la columna A de la hoja de Google.


### When do I get the email?

Sometime between 9-10pm EST Sunday-Thursday. The screener takes about an hour to run and I try to wait a couple hours after market close so that yahoo finance can give me up to date historical data. Also, it is still a work in progress so occasionally errors stop it from running and I have to execute it manually.

## ¿Cuándo recibo el correo electrónico?
En algún momento entre las 9 y las 10 pm EST de domingo a jueves. El evaluador tarda aproximadamente una hora en ejecutarse y trato de esperar un par de horas después del cierre del mercado para que Yahoo Finance pueda proporcionarme datos históricos actualizados. Además, todavía es un trabajo en progreso, por lo que ocasionalmente los errores impiden que se ejecute y tengo que ejecutarlo manualmente.

### Trading Advice

The stocks sent in the email are NOT a buying recommendation. They are simply stocks that could be at a pivotal point in their price action. If you don't understand Ichimoku Cloud or stock charts in general this screener will not be very helpful.

## Asesoramiento de Trading
Las acciones enviadas en el correo electrónico NO son una recomendación de compra. Son simplemente acciones que podrían estar en un punto crucial en la acción del precio. Si no comprende Ichimoku Cloud o los gráficos de acciones en general, este evaluador no será de mucha ayuda.



