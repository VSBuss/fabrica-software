<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saldos</title>
    <link rel="stylesheet" href="../../css/usuarios/saldos.css">
</head>
<body>
    <?php include_once("menu.php") ?>
    <!--TELA SALDOS-->
    <div class="main-carteira">
        <div class="azscore">
            <div class="azcoinscore">
                <span id="textscore">AZCoin</span>
                <div class="valores">
                    <svg width="27" height="21" viewBox="0 0 27 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20.5 1H3.5L2 1.5L1 3V4.5V5.5M1 5.5L3 6.5H5H23L24 7.5L24.5 8V9.5V10M1 5.5V16.5V18L1.5 18.5L2.5 19.5L4 20H21.5H23L24 19L24.5 17.5V16M24.5 10H26V12V16H24.5M24.5 10H20H19L18 10.5L17 11.5L16.5 12.5V14L17.5 15L18.5 16H20H24.5M12.5 13H13M13 13H15.5L10.5 18.5L10 19L5 13H7.5V7.5H12.5H13V13ZM22 4.5H3.5L3 4V3.5L4 3H21H21.5" stroke="#0A2334" stroke-linecap="round"/>
                        <circle cx="19.9502" cy="12.9502" r="0.75" fill="#0A2334"/>
                    </svg>
                    <img id="azcoin" src="../../img/moedaAZ.png" height="27" width="28">
                    <span id="">10.950</span>
                </div>
            </div>
    
            <div class="azmeritscore">
                <span id="textscore">AZMerit</span>
                <div class="valores">
                    <svg width="27" height="21" viewBox="0 0 27 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20.5 1H3.5L2 1.5L1 3V4.5V5V5.5M1 5.5L3.5 6.5H22L23.5 7L24.5 8V9.5V10H26V16H24.5V17.5V18.5L22.5 20H4L2 19.5L1 18V5.5ZM24 10H19.5L17.5 11L17 12L16.5 13L17 14.5L18 15.5L19.5 16H24M22 4.5H4L3 4L3.5 3H4H21M15 13.5H13V19H7.5V13.5H5L10 8L15 13.5Z" stroke="#0A2334" stroke-linecap="round"/>
                        <circle cx="19.9502" cy="12.9502" r="0.75" fill="#0A2334"/>
                    </svg>
                    <img id="azcoin" src="../../img/moedaAZ.png" height="27" width="28">
                    <span>00.00</span>
                </div>
            </div>
        </div>
    
        <div class="main-score-history">
            <span>Histórico de Transação</span>
            <div class="div-principal">
                <img class="mr-yellow" src="../../img/mr-yellow.png">
                <div class="div-table">
                    <span class="">RECEBIDOS</span>
                    <table class="table-score">
                        <thead class="thead-score">
                            <tr class="tr-table">
                                <!--Nome, valor e data-->
                                <th>Nome</th>
                                <th>Valor</th>
                                <th>Data</th>
                            </tr>
                        </thead>
                        <tbody class="tbody-score">
    
                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>
    
                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>
    
                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>
    
                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>
    
                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>
    
                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>

                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>

                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>

                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>

                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>

                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>
                            
                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>

                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>

                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>

                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>

                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>

                            <tr>
                                <!--Nome-->
                                <td>
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>

                            
    
                        </tbody>
                    </table>
                </div>
                <hr class="linha-divisoria"></hr>
                <div class="div-table">
                    <span>ENVIADOS</span>
                    <table class="table-score">
                        <thead class="thead-score">
                            <tr class="tr-table">
                                <!--Nome, valor e data-->
                                <th>Nome</th>
                                <th>Valor</th>
                                <th>Data</th>
                            </tr>
                        </thead>
                        <tbody class="tbody-score">
                            <tr>
                                <!--Nome-->
                                <td class="element-table">
                                    <img src="../../img/transDar.png" height="38px" width="45px" alt="">
                                    <span>Vitor</span>
                                </td>
                                <!--Valor-->
                                <td>
                                    <img src="../../img/moedaAZ.png" height="38" width="38" alt="">
                                    <span>25,00</span>
                                </td>
                                <!--Data-->
                                <td>
                                    <span class="data">28/02/2023</span>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    </div>
</body>
</html>