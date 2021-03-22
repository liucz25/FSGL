/**
 * 保存文件到本地
 * @param {*} options 参数
 */
 export const saveLocalFile: SaveFileFunction = (options) => {
    const { filename, type, content } = options
    const name = `${filename}.${type}`
    if (window.Blob) {
      const blob = content instanceof Blob ? content : getExportBlobByContent(XEUtils.toValueString(content), options)
      if (navigator.msSaveBlob) {
        navigator.msSaveBlob(blob, name)
      } else {
        const linkElem = document.createElement('a')
        linkElem.target = '_blank'
        linkElem.download = name
        linkElem.href = URL.createObjectURL(blob)
        document.body.appendChild(linkElem)
        linkElem.click()
        document.body.removeChild(linkElem)
      }
      return Promise.resolve()
    }
    return Promise.reject(new Error(UtilTools.getLog('vxe.error.notExp')))
  }