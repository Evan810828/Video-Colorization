import './App.css';
import {Button, Upload} from '@douyinfe/semi-ui';
import { IconPlus } from '@douyinfe/semi-icons';
import { useEffect, useState } from 'react';

function App() {
  const action = '/api/login/account';
  const [Origfile, setOrig] = useState([]);
  const [Hairfile, setHair] = useState([]);
  const [Clothfile, setCloth] = useState([]);
  
  var base64_code = {
    origin: undefined,
    hair: undefined,
    cloth: undefined,
  }

  const handleProgress = (options) => {
    const { onSuccess, onError, file, onProgress } = options;
    console.log(options)

    const reader = new FileReader();
    reader.readAsDataURL(file.fileInstance)

    reader.onload = (file) => {
      console.log(file)
      const params = {
        code: file.target.result, // 把 本地图片的base64编码传给后台，调接口，生成图片的url
      };

      // downloadFile(params.myBase64, "filename")
      fetch("http://127.0.0.1/api/upload/",{
        method:"POST",
        body: JSON.stringify({code: params.code}),
      }).then(resp=>{
        return resp.json()
      }).then(data=>{
        console.log(data)
      })

      onSuccess()
      return params.code;
    }
  }

  const colorize = () => {

  }
  
  return (
    <div className="App">
      <div className="App-header">
        <div>
          <div>
            <div>Original Image</div>
            <div style={{"justifyContent":"center", "display":"flex","marginBottom":"50px","marginTop":"10px"}}>
            <Upload
              limit={1}
              fileList={Origfile}
              customRequest={(options) => {base64_code.origin = handleProgress(options)}}
              onChange={(e) => {setOrig(e.fileList)}}
              listType="picture"
              action={action}
            >
              <IconPlus size="extra-large" />
            </Upload>
            </div>
          </div>
          {/* <div>
            <div>Hair Reference</div>
            <div style={{"justifyContent":"center", "display":"flex","marginBottom":"50px","marginTop":"10px"}}>
            <Upload
              limit={1}
              fileList={Hairfile}
              customRequest={(options) => {base64_code.hair = handleProgress(options)}}
              onChange={(e) => {setHair(e.fileList)}}
              listType="picture"
              action={action}
            >
              <IconPlus size="extra-large" />
            </Upload>
            </div>
          </div> */}
          {/* <div>
            <div>Cloth Reference</div>
            <div style={{"justifyContent":"center", "display":"flex","marginBottom":"50px","marginTop":"10px"}}>
            <Upload
              limit={1}
              fileList={Clothfile}
              customRequest={(options) => {base64_code.cloth = handleProgress(options)}}
              onChange={(e) => {setCloth(e.fileList); setCookie("base64_code", base64_code);}}
              listType="picture"
              action={action}
            >
              <IconPlus size="extra-large" />
            </Upload>
            </div>
          </div> */}
        </div>
        <Button theme='solid' className='bu' onClick={() => {colorize();}}>
          Segment
        </Button>
        <div>
          Result
        </div>
      </div>
    </div>
  );
}

export default App;
