
class Api:
    class URLS:
        BENFICIARY_OR_25_PERCENT_BASE_URL = 'http://192.168.50.226:8099/Olams-Portal/Loanee/get-loanee-balance-details-for-application'
    
        NECTA_APPLICANT_INFORMATION_BASE_URL = "https://api.necta.go.tz/api/particulars/individual"

        CONTROL_NUMBER_BASE_URL  = "http://192.168.50.226:8070/api/v1/GePG/requestControlNo"

        CHECK_CONTROL_NUMBER_STATUS_BASE_URL = "http://192.168.50.226:8070/api/v1/GePG/getControlNoRequestStatus?bill"

        CONTROL_NUMBER_INFOS_BASE_URL = "http://192.168.50.226:8070/api/v1/GePG/getControlNoInformation"

    class Methods:
        POST = "POST"
        GET = "GET"
