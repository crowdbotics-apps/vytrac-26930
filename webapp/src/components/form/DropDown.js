import React, {Component} from 'react';

const SUPPORTED_ORIENTATIONS = ['portrait', 'portrait-upside-down', 'landscape', 'landscape-left', 'landscape-right'];

class DropDown extends Component {
  constructor(props) {
    super(props);

    this.state = {
      options: props.options ? props.options : []
    };
  }

  render() {
    let _this = this;
    return (
      <div className="position-front" style={{ overflow: 'scroll', backgroundColor: 'white', marginTop: 0, height: this.props.height ? this.props.height : 150, maxHeight: this.props.height ? this.props.height : 150, borderBottomRightRadius: 5, borderBottomLeftRadius: 5, border: '1px solid #D4E7FA'}}>
        {this.state.options.map((item, key) => {
          return (
            <div key={key} onClick={()=>_this.props.return(item)}>
              {this.props.renderItem ? this.props.renderItem(item) : <div style={{
                color: 'black',
                padding: 10,
                fontSize: '1vw',
                backgroundColor: 'white'
              }}>
                {item.label ? item.label : (item ? item : '')}
              </div>}
            </div>
          );
        })}
      </div>
    );
  }
}

export default DropDown;
