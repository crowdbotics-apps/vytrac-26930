import React, { Component, View } from 'react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import '../../App.css';

import {store} from '../../util/store'

import DropDown from '../../components/form/DropDown';

import eyeIcon from '../../assets/icons/eye_open.png';
import arrowIcon from '../../assets/icons/arrow_down.png';

class LoginForm extends Component {

  constructor(props) {
    store.init();
    super(props);
    this.state = {
      hidePass: true,
      timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
      timezones: [
        'Australian Central Daylight Savings Time',
        'Australian Central Standard Time',
        'Acre Time',
        'Australian Central Western Standard Time',
        'Atlantic Daylight Time',
        'Australian Eastern Daylight Savings Time',
        'Australian Eastern Standard Time',
        'Afghanistan Time',
        'Alaska Daylight Time',
        'Alaska Standard Time',
        'Amazon Summer Time',
        'Amazon Time',
        'Armenia Time',
        'Argentina Time',
        'Atlantic Standard Time',
        'Arabia Standard Time',
        'Atlantic Time',
        'Australian Western Standard Time',
        'Azores Summer Time',
        'Azores Standard Time',
        'Azerbaijan Time',
        'Brunei Time',
        'Baker Island Time',
        'Brunei Darussalam Time',
        'Bolivia Time',
        'Brasilia Summer Time',
        'Brasilia Time',
        'British Summer Time',
        'Bangladesh Standard Time',
        'Bougainville Standard Time',
        'Bhutan Time',
        'Central Africa Time',
        'Cocos Islands Time',
        'Central Daylight Time',
        'Cuba Daylight Time',
        'Central European Summer Time',
        'Central European Time',
        'Chatham Daylight Time',
        'Chatham Standard Time',
        'Choibalsan Summer Time',
        'Choibalsan Standard Time',
        'Chamorro Standard Time',
        'Chuuk Time',
        'Clipperton Island Standard Time',
        'Central Indonesia Time',
        'Cook Island Time',
        'Chile Summer Time',
        'Chile Standard Time',
        'Colombia Summer Time',
        'Colombia Time',
        'Central Standard Time',
        'Cuba Standard Time',
        'China Standard Time',
        'Central Time',
        'Cape Verde Time',
        'Central Western Standard Time',
        'Christmas Island Time',
        'Davis Time',
        'Dumont dUrville Time',
        'Easter Island Summer Time',
        'Easter Island Standard Time',
        'East Africa Time',
        'Ecuador Time',
        'Eastern Daylight Time',
        'Eastern European Summer Time',
        'Eastern European Time',
        'Eastern Greenland Summer Time',
        'Eastern Greenland Time',
        'Eastern Indonesian Time',
        'Eastern Standard Time',
        'Eastern Time',
        'Further-eastern European Time',
        'Fiji Time',
        'Falkland Islands Summer Time',
        'Falkland Islands Time',
        'Fernando de Noronha Time',
        'Galapagos Time',
        'Gambier Islands',
        'Georgia Standard Time',
        'French Guiana Time',
        'Gilbert Island Time',
        'Gambier Island Time',
        'Greenwich Mean Time',
        'Gulf Standard Time',
        'South Georgia Time',
        'Guyana Time',
        'Hawaii-Aleutian Daylight Time',
        'Hawaii-Aleutian Standard Time',
        'Hong Kong Time',
        'Heard and McDonald Islands Time',
        'Khovd Summer Time',
        'Khovd Standard Time',
        'Indochina Time',
        'Israel Daylight Time',
        'Indian Chagos Time',
        'Iran Daylight Time',
        'Irkutsk Time',
        'Iran Standard Time',
        'Indian Standard Time',
        'Irish Standard Time',
        'Israel Standard Time',
        'Japan Standard Time',
        'Kyrgyzstan time',
        'Kosrae Time',
        'Krasnoyarsk Time',
        'Korea Standard Time',
        'Lord Howe Daylight Time',
        'Lord Howe Standard Time',
        'Line Islands Time',
        'Magadan Time',
        'Marquesas Islands Time',
        'Mawson Station Time',
        'Mountain Daylight Time',
        'Marshall Islands',
        'Macquarie Island Station Time',
        'Marquesas Islands Time',
        'Myanmar Standard Time',
        'Moscow Time',
        'Mountain Standard Time',
        'Malaysia Standard Time',
        'Mountain Time',
        'Mauritius Time',
        'Maldives Time',
        'Malaysia Time',
        'New Caledonia Time',
        'Newfoundland Daylight Time',
        'Norfolk Time',
        'Nepal Time',
        'Nauru Time',
        'Newfoundland Standard Time',
        'Newfoundland Time',
        'Niue Time',
        'New Zealand Daylight Time',
        'New Zealand Standard Time',
        'Omsk Time',
        'Oral Time',
        'Pacific Daylight Time',
        'Peru Time',
        'Kamchatka Time',
        'Papua New Guinea Time',
        'Phoenix Island Time',
        'Philippine Time',
        'Pakistan Standard Time',
        'Saint Pierre and Miquelon Daylight time',
        'Saint Pierre and Miquelon Standard Time',
        'Pohnpei Standard Time',
        'Pacific Standard Time',
        'Philippine Standard Time',
        'Pacific Time',
        'Palau Time',
        'Paraguay Summer Time',
        'Paraguay Time',
        'Réunion Time',
        'Rothera Research Station Time',
        'Sakhalin Island time',
        'Samara Time',
        'South African Standard Time',
        'Solomon Islands Time',
        'Seychelles Time',
        'Singapore Time',
        'Sri Lanka Standard Time',
        'Srednekolymsk Time',
        'Suriname Time',
        'Samoa Standard Time',
        'Showa Station Time',
        'Tahiti Time',
        'French Southern and Antarctic Time',
        'Thailand Standard Time',
        'Tajikistan Time',
        'Tokelau Time',
        'Timor Leste Time',
        'Turkmenistan Time',
        'Tonga Time',
        'Turkey Time',
        'Tuvalu Time',
        'Ulaanbaatar Summer Time',
        'Ulaanbaatar Standard Time',
        'Kaliningrad Time',
        'Coordinated Universal Time',
        'Uruguay Summer Time',
        'Uruguay Standard Time',
        'Uzbekistan Time',
        'Venezuelan Standard Time',
        'Vladivostok Time',
        'Volgograd Time',
        'Vostok Station Time',
        'Vanuatu Time',
        'Wake Island Time',
        'West Africa Summer Time',
        'West Africa Time',
        'Western European Summer Time',
        'Western European Time',
        'Wallis and Futuna Time',
        'West Greenland Time',
        'West Greenland Summer Time',
        'Western Indonesia Time',
        'Eastern Indonesia Time',
        'Western Standard Time',
        'Yakutsk Time',
        'Yekaterinburg Time',
      ],
      allTimeZones: [
        'Australian Central Daylight Savings Time',
        'Australian Central Standard Time',
        'Acre Time',
        'Australian Central Western Standard Time',
        'Atlantic Daylight Time',
        'Australian Eastern Daylight Savings Time',
        'Australian Eastern Standard Time',
        'Afghanistan Time',
        'Alaska Daylight Time',
        'Alaska Standard Time',
        'Amazon Summer Time',
        'Amazon Time',
        'Armenia Time',
        'Argentina Time',
        'Atlantic Standard Time',
        'Arabia Standard Time',
        'Atlantic Time',
        'Australian Western Standard Time',
        'Azores Summer Time',
        'Azores Standard Time',
        'Azerbaijan Time',
        'Brunei Time',
        'Baker Island Time',
        'Brunei Darussalam Time',
        'Bolivia Time',
        'Brasilia Summer Time',
        'Brasilia Time',
        'British Summer Time',
        'Bangladesh Standard Time',
        'Bougainville Standard Time',
        'Bhutan Time',
        'Central Africa Time',
        'Cocos Islands Time',
        'Central Daylight Time',
        'Cuba Daylight Time',
        'Central European Summer Time',
        'Central European Time',
        'Chatham Daylight Time',
        'Chatham Standard Time',
        'Choibalsan Summer Time',
        'Choibalsan Standard Time',
        'Chamorro Standard Time',
        'Chuuk Time',
        'Clipperton Island Standard Time',
        'Central Indonesia Time',
        'Cook Island Time',
        'Chile Summer Time',
        'Chile Standard Time',
        'Colombia Summer Time',
        'Colombia Time',
        'Central Standard Time',
        'Cuba Standard Time',
        'China Standard Time',
        'Central Time',
        'Cape Verde Time',
        'Central Western Standard Time',
        'Christmas Island Time',
        'Davis Time',
        'Dumont dUrville Time',
        'Easter Island Summer Time',
        'Easter Island Standard Time',
        'East Africa Time',
        'Ecuador Time',
        'Eastern Daylight Time',
        'Eastern European Summer Time',
        'Eastern European Time',
        'Eastern Greenland Summer Time',
        'Eastern Greenland Time',
        'Eastern Indonesian Time',
        'Eastern Standard Time',
        'Eastern Time',
        'Further-eastern European Time',
        'Fiji Time',
        'Falkland Islands Summer Time',
        'Falkland Islands Time',
        'Fernando de Noronha Time',
        'Galapagos Time',
        'Gambier Islands',
        'Georgia Standard Time',
        'French Guiana Time',
        'Gilbert Island Time',
        'Gambier Island Time',
        'Greenwich Mean Time',
        'Gulf Standard Time',
        'South Georgia Time',
        'Guyana Time',
        'Hawaii-Aleutian Daylight Time',
        'Hawaii-Aleutian Standard Time',
        'Hong Kong Time',
        'Heard and McDonald Islands Time',
        'Khovd Summer Time',
        'Khovd Standard Time',
        'Indochina Time',
        'Israel Daylight Time',
        'Indian Chagos Time',
        'Iran Daylight Time',
        'Irkutsk Time',
        'Iran Standard Time',
        'Indian Standard Time',
        'Irish Standard Time',
        'Israel Standard Time',
        'Japan Standard Time',
        'Kyrgyzstan time',
        'Kosrae Time',
        'Krasnoyarsk Time',
        'Korea Standard Time',
        'Lord Howe Daylight Time',
        'Lord Howe Standard Time',
        'Line Islands Time',
        'Magadan Time',
        'Marquesas Islands Time',
        'Mawson Station Time',
        'Mountain Daylight Time',
        'Marshall Islands',
        'Macquarie Island Station Time',
        'Marquesas Islands Time',
        'Myanmar Standard Time',
        'Moscow Time',
        'Mountain Standard Time',
        'Malaysia Standard Time',
        'Mountain Time',
        'Mauritius Time',
        'Maldives Time',
        'Malaysia Time',
        'New Caledonia Time',
        'Newfoundland Daylight Time',
        'Norfolk Time',
        'Nepal Time',
        'Nauru Time',
        'Newfoundland Standard Time',
        'Newfoundland Time',
        'Niue Time',
        'New Zealand Daylight Time',
        'New Zealand Standard Time',
        'Omsk Time',
        'Oral Time',
        'Pacific Daylight Time',
        'Peru Time',
        'Kamchatka Time',
        'Papua New Guinea Time',
        'Phoenix Island Time',
        'Philippine Time',
        'Pakistan Standard Time',
        'Saint Pierre and Miquelon Daylight time',
        'Saint Pierre and Miquelon Standard Time',
        'Pohnpei Standard Time',
        'Pacific Standard Time',
        'Philippine Standard Time',
        'Pacific Time',
        'Palau Time',
        'Paraguay Summer Time',
        'Paraguay Time',
        'Réunion Time',
        'Rothera Research Station Time',
        'Sakhalin Island time',
        'Samara Time',
        'South African Standard Time',
        'Solomon Islands Time',
        'Seychelles Time',
        'Singapore Time',
        'Sri Lanka Standard Time',
        'Srednekolymsk Time',
        'Suriname Time',
        'Samoa Standard Time',
        'Showa Station Time',
        'Tahiti Time',
        'French Southern and Antarctic Time',
        'Thailand Standard Time',
        'Tajikistan Time',
        'Tokelau Time',
        'Timor Leste Time',
        'Turkmenistan Time',
        'Tonga Time',
        'Turkey Time',
        'Tuvalu Time',
        'Ulaanbaatar Summer Time',
        'Ulaanbaatar Standard Time',
        'Kaliningrad Time',
        'Coordinated Universal Time',
        'Uruguay Summer Time',
        'Uruguay Standard Time',
        'Uzbekistan Time',
        'Venezuelan Standard Time',
        'Vladivostok Time',
        'Volgograd Time',
        'Vostok Station Time',
        'Vanuatu Time',
        'Wake Island Time',
        'West Africa Summer Time',
        'West Africa Time',
        'Western European Summer Time',
        'Western European Time',
        'Wallis and Futuna Time',
        'West Greenland Time',
        'West Greenland Summer Time',
        'Western Indonesia Time',
        'Eastern Indonesia Time',
        'Western Standard Time',
        'Yakutsk Time',
        'Yekaterinburg Time',
      ]
    }
  }

  validate () {
    if (!this.state.username) {
      alert("Please fill your username");
      return false;
    } else if (!this.state.password) {
      alert("Please fill your password");
      return false;
    } else {
      return true;
    }
  }

  login() { 
    if(this.validate()) {
      try {
        console.log(this.state.username, this.state.password);
        store.data.login(this.state.username, this.state.password).then((result) => {
          if(result) {
            this.props.changeItem('login-token');
          } else {
            alert("Could not login:");
          }
        });
        
      } catch (ex) {
        alert("Could not login");
      }
    }
  }

  resetPassword() { 
    this.props.changeItem('reset-password');
  }

  showDropDown() {
    if(this.state.showDropDown) {
      return (
        <DropDown 
          return={(timezone) => {this.setState({timezone: timezone, showDropDown: false })}}
          options={this.state.timezones}>
        </DropDown>
      )
    } else {
      return null;
    }
  }

  filterTimeZone (timezone) {
    var items = [];
    if(!timezone) {
      items = this.state.allTimeZones;
    } else {
      for (var i = 0; i < this.state.allTimeZones.length; i++) {
        if(this.state.allTimeZones[i].includes(timezone)) {
          items.push(this.state.allTimeZones[i])
        }
      }
    }
    this.setState({timezones: items, showDropDown: false}, () => {
      this.setState({showDropDown: true})
    });
  }

  render() {
    return (
        <div style={{height: '100%'}}> 
          <Row className="vertical-container">
            <Col className="line-container">
              <div className="green-line"></div>
            </Col>
            <Col className="line-container">
              <div className="grey-line"></div>
            </Col>
          </Row>  
          <p className="text-left">Welcome to <span className="bold-blue text-bolder">VyTrac</span></p>

          <p className="text-left dynamic-font-normal">Lorem ipsum dolor sit amet, cons cdipiscing elit. Duis non turpis nec nunc </p>

          <p className="grey-text username-label dynamic-font-normal">Username, Email or Phone number</p>
          <input onChange={(username) => this.setState({username: username.target.value})} className="text-field dynamic-font-normal" type="text" name="username" />
          <p className="grey-text password-label dynamic-font-normal">Password</p>
          <div>
            <input onChange={(password) => this.setState({password: password.target.value})} className="text-field dynamic-font-normal" type={this.state.hidePass ? 'password' : 'text'} name="password" />
            <img className="textfield-button" resizeMode={'stretch'} onClick={() => this.setState({hidePass: !this.state.hidePass})} src={eyeIcon}></img>
          </div>
          
          <p className="grey-text password-label dynamic-font-normal">Your time zone</p>
          <div>
            <input onChange={(timezone) => {this.setState({timezone: timezone.target.value}); this.filterTimeZone(timezone.target.value);}} value={this.state.timezone} className="text-field dynamic-font-normal" name="timezone" />  
            <img className="textfield-button" style={{marginLeft: '-3%', maxWidth: '2%', maxHeight: '2%'}} resizeMode={'stretch'} onClick={() => this.setState({showDropDown: !this.state.showDropDown})} src={arrowIcon}></img> 
            {this.showDropDown()}
          </div>
          

          <Row className="vertical-container remember-me">
            <Col style={{padding: 0, margin: 0}}  xs={12}>
              <input type="checkbox" className="greycheck dynamic-font-normal" checked={this.state.rememberMe} onChange={() => this.setState({rememberMe: !this.state.rememberMe})} />
              <span className="grey-text dynamic-font-normal">&nbsp;&nbsp;&nbsp;&nbsp;Remember me</span>
            </Col>
          </Row>

          <Row className="bottom-button-container">
            <Col xs={2}>
              <Button className="dynamic-font-normal text-bold" onClick={() => this.resetPassword()} style={{marginRight: '50%'}} variant="light">FORGOT PASSWORD</Button>
            </Col>
            <Col xs={8}>
            </Col>
            <Col xs={2}>
              <Button className="dynamic-font-normal text-bold" onClick={() => this.login()}>LOGIN</Button>
            </Col>
          </Row>
        </div>
    );
  }
}

export default LoginForm;