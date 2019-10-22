import React from 'react'
import ReactDOM from 'react-dom'
import * as serviceWorker from './serviceWorker'
import './index.css'

var data = require('./your_file.json');

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      nian: 'Skriv in nio bokstäver för att se om det är ett ord.',
    };


    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
    this.setState({nian: ''})
    if (event.target.value.length == 9){
      if (data.includes(event.target.value.toLowerCase())){
        this.setState({nian: event.target.value+' ÄR ett nianord!'})
        }else{
          this.setState({nian: event.target.value.toLowerCase()+' ÄR INTE ett nianord...'})
        }
      
    }
  }



  render() {
    return (
      <div className="App">
        <form>
            <textarea value={this.state.value} onChange={this.handleChange} cols={40} rows={4} />
        </form>
        <div className="preview">
          <h1>{this.state.nian}</h1>
        </div>
      </div>
    );
  }
}

export default App