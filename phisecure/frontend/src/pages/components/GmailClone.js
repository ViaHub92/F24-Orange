import logo from './phimail.png';
import Inbox from './Inbox';

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
          <span className="material-icons"> menu </span>
          <img src="https://i.pinimg.com/originals/ae/47/fa/ae47fa9a8fd263aa364018517020552d.png" alt="" />
        </div>
        <div className="header__middle">
          <span className="material-icons"> search </span>
          <input type="text" placeholder="Search mail" />
          <span className="material-icons"> arrow_drop_down </span>
        </div>
        <div className="header__right">
          <span className="material-icons"> apps </span>
          <span className="material-icons"> notifications </span>
          <span className="material-icons"> account_circle </span>
        </div>
      </div>
      {/* Header Ends */}
      {/* Main Body Starts */}
      <div className="main__body">
        {/* Sidebar Starts */}
        <div className="sidebar">
          <button className="sidebar__compose"><span className="material-icons"> add </span>Compose</button>
          <div className="sidebarOption sidebarOption__active">
            <span className="material-icons"> inbox </span>
            <h3>Inbox</h3>
          </div>
          <div className="sidebarOption">
            <span className="material-icons"> star </span>
            <h3>Starred</h3>
          </div>
          <div className="sidebarOption">
            <span className="material-icons"> access_time </span>
            <h3>Snoozed</h3>
          </div>
          <div className="sidebarOption">
            <span className="material-icons"> label_important </span>
            <h3>Important</h3>
          </div>
          <div className="sidebarOption">
            <span className="material-icons"> near_me </span>
            <h3>Sent</h3>
          </div>
          <div className="sidebarOption">
            <span className="material-icons"> note </span>
            <h3>Drafts</h3>
          </div>
          <div className="sidebarOption">
            <span className="material-icons"> expand_more </span>
            <h3>More</h3>
          </div>
          <div className="sidebar__footer">
            <div className="sidebar__footerIcons">
              <span className="material-icons"> person </span>
              <span className="material-icons"> duo </span>
              <span className="material-icons"> phone </span>
            </div>
          </div>
        </div>
        {/* Sidebar Ends */}
        {/* Email List Starts */}
        <div className="emailList">
          {/* Settings Starts */}
          <div className="emailList__settings">
            <div className="emailList__settingsLeft">
              <input type="checkbox" />
              <span className="material-icons"> arrow_drop_down </span>
              <span className="material-icons"> redo </span>
              <span className="material-icons"> more_vert </span>
            </div>
            <div className="emailList__settingsRight">
              <span className="material-icons"> chevron_left </span>
              <span className="material-icons"> chevron_right </span>
              <span className="material-icons"> keyboard_hide </span>
              <span className="material-icons"> settings </span>
            </div>
          </div>
          {/* Settings Ends */}
          {/* Section Starts */}
          <div className="emailList__sections">
            <div className="section section__selected">
              <span className="material-icons"> inbox </span>
              <h4>Primary</h4>
            </div>
            <div className="section">
              <span className="material-icons"> people </span>
              <h4>Social</h4>
            </div>
            <div className="section">
              <span className="material-icons"> local_offer </span>
              <h4>Promotions</h4>
            </div>
          </div>
          {/* Section Ends */}
          {/* Email List rows starts */}
          
          <div className="email-list">
          <Inbox />
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