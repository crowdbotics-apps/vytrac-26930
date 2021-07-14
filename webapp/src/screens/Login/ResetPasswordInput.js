import React, { Component, View } from 'react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import '../../App.css';

import {store} from '../../util/store'

import passwordLogo from '../../assets/images/password.png';
import eyeIcon from '../../assets/icons/eye_open.png';

class LoginForm extends Component {

  constructor(props) {
    store.init();
    super(props);
    this.state = {
      validatePass1: '',
      validatePass2: '',
      validatePass1Text: '',
      validatePass2Text: '',
      hidePass1: true,
      hidePass2: true
    }
  }

  validatePass1 (pass) {
    console.log(pass);
    if (!pass) {
      this.setState({
        validatePass1: 'red'
      })
    } else {
      if (pass.length < 8) {
        this.setState({
          validatePass1: 'red',
          validatePass1Text: 'Password must be 8 characters of length'
        })
      } else if (!(/\d/.test(pass))) {
        this.setState({
          validatePass1: 'red',
          validatePass1Text: 'Password must contain at least one number'
        })
      } else if (!(/[~`!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/g.test(pass))){
        this.setState({
          validatePass1: 'red',
          validatePass1Text: 'Password must contain at least one special character'
        })
      } else {
        this.setState({
          validatePass1: '',
          validatePass1Text: ''
        })
      }
    }
  }

  validatePass2 (pass) {
    console.log(pass, this.state.password1, this.state.password1 != pass)
    if (!pass) {
      this.setState({
        validatePass2: 'red'
      })
    } else {
      if(pass != this.state.password1) {
        this.setState({
          validatePass2: 'red',
          validatePass2Text: 'Passwords must match'
        })
      } else {
        this.setState({
          validatePass2: '',
          validatePass2Text: ''
        })
      }
    }
  }

  validate () {
    if (!this.state.password1) {
      alert("Please fill your username");
      return false;
    } else if (!this.state.password2) {
      alert("Please fill your password");
      return false;
    } else {
      return true;
    }
  }

  login() { 
    if(this.validate()) {
      try {
        store.data.login(this.state.username + '', this.state.password + '').then((result) => {
          if(result) {
            alert("Successful login!");
          } else {
            alert("Could not login");
          }
        });
      } catch (ex) {
        alert("Could not login");
      }
    }
  }

  gotNumber(fieldIndex) {
    const nextSibling = document.querySelector(
      `input[name=number${fieldIndex + 1}]`
    );
    // If found, focus the next field
    if (nextSibling !== null) {
      nextSibling.focus();
    }
  }

  render() {
    return (
        <div> 
            <Row className="vertical-container">
                <Col className="line-container">
                  <div className="grey-line-inv"></div>
                </Col>
                <Col className="line-container">
                  <div className="green-line-inv"></div>
                </Col>
              </Row>  

              <div className="centered-logo">
                <div className="logo-container">
                  <img className="shield-logo" resizeMode={'stretch'} src={passwordLogo}></img>
                </div>
              </div>

              <p className="text-left normal-text dynamic-font-heading" style={{marginTop: 30}}>Reset my password</p>

              <p className="text-left smaller-text dynamic-font-normal">Set your new password</p>

              <p className="grey-text password-label top15 dynamic-font-normal">Password</p>
              <div>
                <input style={{borderBottomColor: this.state.validatePass1}} onChange={(username) => { this.setState({password1: username.target.value}); this.validatePass1(username.target.value); }} className="text-field dynamic-font-normal" type={this.state.hidePass1 ? 'password' : 'text'} name="password1" />
                <img className="textfield-button" resizeMode={'stretch'} onClick={() => this.setState({hidePass1: !this.state.hidePass1})} src={eyeIcon}></img>
              </div>
              <p className="grey-text password-label dynamic-font-small" style={{fontSize: 8, marginTop: 5, color: this.state.validatePass1}}>{this.state.validatePass1Text}</p>

              <p className="grey-text password-label dynamic-font-normal">Confirm password</p>
              <div>
                <input style={{borderBottomColor: this.state.validatePass2}} onChange={(username) => { this.setState({password2: username.target.value});  this.validatePass2(username.target.value); }} className="text-field dynamic-font-normal" type={this.state.hidePass2 ? 'password' : 'text'} name="password2" />
                <img className="textfield-button" resizeMode={'stretch'} onClick={() => this.setState({hidePass2: !this.state.hidePass2})} src={eyeIcon}></img>
              </div>
              <p className="grey-text password-label dynamic-font-small" style={{fontSize: 8, marginTop: 5, color: this.state.validatePass2}}>{this.state.validatePass2Text}</p>

              <Row className="bottom-button-container">
                <Col xs={2}>
                  <Button onClick={() => this.props.changeItem('login')} style={{marginRight: '55%'}}  variant="light" className="dynamic-font-normal text-bold">CANCEL</Button>
                </Col>
                <Col xs={7}>
                </Col>
                <Col xs={2}>
                  <Button disabled={(this.state.validatePass1 != '' || this.state.validatePass2 != '') || (!this.state.password1 || !this.state.password2) } onClick={() => this.login()} className="dynamic-font-normal text-bold">CONTINUE</Button>
                </Col>
              </Row>
        </div>
    );
  }
}

export default LoginForm;