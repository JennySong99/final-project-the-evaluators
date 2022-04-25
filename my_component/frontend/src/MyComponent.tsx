import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

interface State {
  currPage: number
}

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class MyComponent extends StreamlitComponentBase<State> {

  constructor(props:any) {
    super(props);
    this.state = {
      currPage: this.props.args["currPage"]
    }
    Streamlit.setComponentValue({"currPage": 0});
  }

  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.

    // Streamlit sends us a theme object via props that we can use to ensure
    // that our component has visuals that match the active theme in a
    // streamlit app.
    

    // Maintain compatibility with older versions of Streamlit that don't send
    // a theme object.
  

    // Show a button and some text.
    // When the button is clicked, we'll increment our "numClicks" state
    // variable, and send its new value back to Streamlit, where it'll
    // be available to the Python program.
    return (
      <div>{this.pageContent()}</div>
    )
  }

  public page0 = () => (
    <div className="d-flex justify-content-between">
      <button
          onClick={this.handleHome}
          className="btn btn-light"
        >
          Home
        </button>
        <button
          onClick={this.handleCompareCourse}
          className="btn btn-light"
        >
          Compare Courses
        </button>
        <button
          onClick={this.handleCompareDepartment}
          className="btn btn-light"
        >
          Compare Departments
        </button>
        <button
          onClick={this.handleCompareInstructor}
          className="btn btn-light"
        >
          Compare Instructors
        </button>
    
    </div>
  )


  private pageContent = (): any => {
    return this.page0();
  }


  /** Click handler for our "Click Me!" button. */
  private handleHome = (): void => {
    // Increment state.numClicks, and pass the new value back to
    // Streamlit via `Streamlit.setComponentValue`.
    this.setState(
      { currPage: 0 },
    )

    Streamlit.setComponentValue(
      { currPage: 0 }
    );
  }

  private handleCompareCourse = (): void => {
    // Increment state.numClicks, and pass the new value back to
    // Streamlit via `Streamlit.setComponentValue`.
    this.setState(
      { currPage: 1 },
    )

    Streamlit.setComponentValue(
      { currPage: 1}
    );
  }

  private handleCompareDepartment = (): void => {
    // Increment state.numClicks, and pass the new value back to
    // Streamlit via `Streamlit.setComponentValue`.
    this.setState(
      { currPage: 2 },
    )

    Streamlit.setComponentValue(
      { currPage: 2 }
    );
  }

  private handleCompareInstructor = (): void => {
    // Increment state.numClicks, and pass the new value back to
    // Streamlit via `Streamlit.setComponentValue`.

    this.setState(
      { currPage: 3 },
    )

    Streamlit.setComponentValue(
      { currPage: 3 }
    );
  }

  /** Focus handler for our "Click Me!" button. */
  // private _onFocus = (): void => {
  //   this.setState({ isFocused: true })
  // }

  /** Blur handler for our "Click Me!" button. */
  // private _onBlur = (): void => {
  //   this.setState({ isFocused: false })
  // }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(MyComponent)
