import logo from './phimail.png';
import { PiFishSimpleBold } from "react-icons/pi";
import { GiFishing } from "react-icons/gi";

/* https://github.com/somanath-goudar/html-css-projects/tree/d0365197c68755a8799987bfa9303bc328e71c25/gmail-clone */
const GmailClone = () => {
      return (
        <div>
          <meta charSet="UTF-8" />
          <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          {/* Google Font Icons */}
          <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
          <link rel="stylesheet" href="styles.css" />
          <title>Final - Gmail Clone</title>
          {/* Header Starts */}
          <div className="header">
            <div className="header__left">
              <img src={logo} alt="" />
            </div>
          </div>
          {/* Header Ends */}
          {/* Main Body Starts */}
          <div className="main__body">
            {/* Sidebar Starts */}
            <div className="sidebar">
              <div className="sidebarOption sidebarOption__active">
                <PiFishSimpleBold size={45} /> 
                <h3>Inbox</h3>
              </div>
              <div className="sidebarOption">
                <GiFishing size={45} />
                <h3>Spam</h3>
              </div>        
            </div>
            {/* Sidebar Ends */}
            {/* Email List Starts */}
            <div className="emailList">
              {/* Settings Starts */}
              <div className="emailList__settings">
              </div>
              {/* Settings Ends */}
              {/* Section Starts */}
              <div className="emailList__sections">
                <div className="section section__selected">
                  <span className="material-icons"> inbox </span>
                  <h4>Primary</h4>
                </div>
              </div>
              {/* Section Ends */}
              {/* Email List rows starts */}
              <div className="emailList__list">
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber
                      <span className="emailRow__description"> - on Your Channel Future Coders </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber
                      <span className="emailRow__description"> - on Your Channel Future Coders </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber<span className="emailRow__description">
                        - on Your Channel Future Coders
                      </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">Google</h3>
                  <div className="emailRow__message">
                    <h4>
                      Login on New Device<span className="emailRow__description">
                        - is this your Device ?
                      </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">2am</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber
                      <span className="emailRow__description"> - on Your Channel Future Coders </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber
                      <span className="emailRow__description"> - on Your Channel Future Coders </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber<span className="emailRow__description">
                        - on Your Channel Future Coders
                      </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">Google</h3>
                  <div className="emailRow__message">
                    <h4>
                      Login on New Device<span className="emailRow__description">
                        - is this your Device ?
                      </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">2am</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber
                      <span className="emailRow__description"> - on Your Channel Future Coders </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber
                      <span className="emailRow__description"> - on Your Channel Future Coders </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber<span className="emailRow__description">
                        - on Your Channel Future Coders
                      </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">Google</h3>
                  <div className="emailRow__message">
                    <h4>
                      Login on New Device<span className="emailRow__description">
                        - is this your Device ?
                      </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">2am</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber
                      <span className="emailRow__description"> - on Your Channel Future Coders </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber
                      <span className="emailRow__description"> - on Your Channel Future Coders </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber<span className="emailRow__description">
                        - on Your Channel Future Coders
                      </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">Google</h3>
                  <div className="emailRow__message">
                    <h4>
                      Login on New Device<span className="emailRow__description">
                        - is this your Device ?
                      </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">2am</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber
                      <span className="emailRow__description"> - on Your Channel Future Coders </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber
                      <span className="emailRow__description"> - on Your Channel Future Coders </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">YouTube</h3>
                  <div className="emailRow__message">
                    <h4>
                      You Got a New Subscriber<span className="emailRow__description">
                        - on Your Channel Future Coders
                      </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">10pm</p>
                </div>
                {/* Email Row Ends */}
                {/* Email Row Starts */}
                <div className="emailRow">
                  <div className="emailRow__options">
                    <input type="checkbox" name id />
                    <span className="material-icons"> star_border </span>
                    <span className="material-icons"> label_important </span>
                  </div>
                  <h3 className="emailRow__title">Google</h3>
                  <div className="emailRow__message">
                    <h4>
                      Login on New Device<span className="emailRow__description">
                        - is this your Device ?
                      </span>
                    </h4>
                  </div>
                  <p className="emailRow__time">2am</p>
                </div>
                {/* Email Row Ends */}
              </div>
              {/* Email List rows Ends */}
            </div>
            {/* Email List Ends */}
          </div>
          {/* Main Body Ends */}
        </div>
      );
    }

export default GmailClone;