const backendUrl = 'https://vytrac-24106.botics.co/api/v1/';

export class store {

    static data = undefined;

    static init(props){
        if(!this.data) {
            this.data = new StoreConfig();
            this.data.init(props);
            return this.data;
        } else {
            return this.data;
        }
    }

}

class StoreConfig {

    userId = undefined;
    username = undefined;
    name = undefined;
    token = undefined;
    guest = true;
    requestHandler = undefined;
    firebaseToken = undefined;

    init(props) {

    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////// AUTH ////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////

    async login(username, password) {
        var _this = this;
        const data = {
            username: username,
            password: password
        };
        return fetch(backendUrl + "login/", {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
            .then((response) => response.json())
            .then((responseJson) => {
                console.log(responseJson);
                if(responseJson && responseJson.token) {
                    _this.token = responseJson.token;
                    console.log('tokens', _this.token);
                    return true;
                } else {
                    return false;
                }           
            })
            .catch((error) => {
                console.error(error);
            });
    }
}