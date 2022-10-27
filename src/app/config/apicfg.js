const apicfg = {
  "API_BASE_VERSION": "v3"
  ,"API_BASE_URL": "/api/v3"
  ,"WEB_APP_NAME": "pragmatic-nodejs"
  ,"SECRET_KEY": null
  //60 minutes * 24 hours * 8 days = 8 days
  ,"ACCESS_TOKEN_EXPIRE_MINUTES": 60 * 24 * 8
  ,"HOST": "localhost"
  ,"SERVER_NAME": "localhost"
  ,"SERVER_HOST": null
  ,"BACKEND_CORS_ORIGINS": []
  ,"LOG_TIMESTAMP": false
  ,"ALLOWED_FILE_TYPE": [
    '.txt'
    ,'.csv'
    ,'.yml'
    ,'.json'
  ]
  ,"ALLOWED_IMAGE_TYPE": [
    '.pdf'
    ,'.png'
    ,'.jpg'
    ,'.jpeg'
    ,'.tiff'
    ,'.gif'
  ]
  ,"ALLOWED_VIDEO_TYPE": ['.mp4']
  ,"FILE_DELIMITER": ";"
};

export default apicfg;
