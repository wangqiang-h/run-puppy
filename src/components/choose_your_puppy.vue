<template>
    <div class="main-container">
      <div class="top-navigation">
        <div class="status-bar">
          <div class="left-side">
            <div class="status-bar-time"><span class="time">9:41</span></div>
          </div>
          <div class="dynamic-island">
            <div class="status-bar-dynamic-island">
              <div class="true-depth-camera"></div>
              <div class="face-time-camera"></div>
            </div>
          </div>
          <div class="right-side">
            <div class="signal-wifi-battery">
              <div class="icon-mobile-signal"></div>
              <div class="wifi"></div>
              <div class="status-bar-battery"></div>
            </div>
          </div>
        </div>
      </div>
      <span class="choose-your-puppy">Choose your puppy</span>
      <div class="frame">
        <div class="frame-1">
          <div class="image"></div>
          <span class="samoyed">萨摩耶</span>
        </div>
        <div class="frame-2">
          <div class="image-3"></div>
          <span class="teddy">泰迪</span>
        </div>
        <div class="frame-4">
          <div class="group"></div>
          <span class="french-bulldog">法国斗牛犬</span>
        </div>
        <div class="frame-5">
          <div class="image-div"></div>
          <span class="welsh-corgi-span">威尔士柯基</span>
        </div>
        <div class="frame-div">
          <div class="image-div-6"></div>
          <span class="teddy-span">泰迪</span>
        </div>
      </div>
      <div class="slider-container">
      <div class="image-div-7">
        <div class="image-div-8" @click="goToBeforeStarted">
          <div class="rectangle-div"></div>
          <span class="happy-moments-span"> 小快乐也有大美好</span>
          <div class="rectangle"></div>
        </div>
      </div>
      <div class="image-9" @click="goToBeforeStarted">
        <div class="flex-row-fb">
          <div class="rectangle-a"></div>
          <span class="text-content">
            世上或许没有圣诞老人<br />但一定有爱你的人</span
          >
          <div class="rectangle-b"></div>
          <div class="rectangle-c"></div>
        </div>
        <div class="home-indicator"></div>
      </div>
    </div>
  </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';

const router = useRouter();

const goToBeforeStarted = () => {
  router.push({ name: 'before_started' });
};
</script>

  <style scoped>
:root {
  --default-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Ubuntu, "Helvetica Neue", Helvetica, Arial, "PingFang SC",
    "Hiragino Sans GB", "Microsoft Yahei UI", "Microsoft Yahei",
    "Source Han Sans CN", sans-serif;
}

.main-container {
  overflow: hidden;
}

.main-container,
.main-container * {
  box-sizing: border-box;
}

input,
select,
textarea,
button {
  outline: 0;
}

.main-container {
  position: relative;
  width: 393px;
  height: 852px;
  margin: 0 auto;
  background: linear-gradient(180deg, #fffbd7, #fffefe);
  overflow: hidden;
}
.top-navigation {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  gap: 2px;
  position: relative;
  width: 393px;
  margin: 0 0 0 0;
  backdrop-filter: blur(10px);
}
.status-bar {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 59px;
  z-index: 1;
}
.left-side {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 0 3px 10px;
  z-index: 2;
}
.status-bar-time {
  flex-shrink: 0;
  position: relative;
  width: 54px;
  height: 21px;
  z-index: 3;
  border-radius: 24px;
}
.time {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 54px;
  height: 20px;
  top: 1px;
  left: 0;
  color: #000000;
  font-family: SF Pro Text, var(--default-font-family);
  font-size: 16px;
  font-weight: 600;
  line-height: 20px;
  text-align: center;
  white-space: nowrap;
  letter-spacing: -0.32px;
  z-index: 4;
}
.dynamic-island {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  width: 125px;
  min-height: 0;
  z-index: 5;
}
.status-bar-dynamic-island {
  flex-shrink: 0;
  position: relative;
  width: 125px;
  height: 37px;
  background: #000000;
  z-index: 6;
  border-radius: 100px;
}
.true-depth-camera {
  position: absolute;
  width: 80px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(-78.13%, -50%);
  z-index: 7;
  overflow: hidden;
  border-radius: 100px;
}
.face-time-camera {
  position: absolute;
  width: 37px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(68.92%, -50%);
  z-index: 8;
  overflow: hidden;
  border-radius: 100px;
}
.right-side {
  display: flex;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 11px 0 0;
  z-index: 9;
}
.signal-wifi-battery {
  display: flex;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8px;
  position: relative;
  width: 78.401px;
  z-index: 10;
}
.icon-mobile-signal {
  flex-shrink: 0;
  position: relative;
  width: 18px;
  height: 12px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/181640/mobile-signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.wifi {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/181640/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 12;
}
.status-bar-battery {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/181640/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.choose-your-puppy {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: relative;
  width: 194px;
  height: 25px;
  margin: 55px 0 0 100px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20.448429107666016px;
  font-weight: 600;
  line-height: 24.747px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 14;
}
.frame {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 8px;
  position: relative;
  width: 100%; /* 改为100%以利用父容器宽度 */
  padding: 0 20px; /* 添加内边距防止内容贴边 */
  margin: 30px 0 0 0; /* 调整外边距 */
  z-index: 15;
  overflow-x: auto; /* 允许水平滚动 */
  white-space: nowrap; /* 防止子元素换行 */
  -webkit-overflow-scrolling: touch; /* 优化移动端滚动体验 */
  scroll-snap-type: x mandatory; /* 可选：添加滚动吸附效果 */
}
/* 为每个子项添加滚动吸附点（可选） */
.frame > * {
  scroll-snap-align: start;
}

/* 隐藏滚动条 */
.frame::-webkit-scrollbar {
  display: none; /* Chrome, Safari 和 Opera */
}
.frame-1 {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 11px;
  position: relative;
  width: 97px;
  z-index: 16;
}
.image {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 97px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/181640/samoyed-puppy.png)
    no-repeat center;
  background-size: cover;
  z-index: 17;
  border-radius: 10px;
}
.samoyed {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  min-width: 0;
  height: 15px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 18;
}
.frame-2 {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 11px;
  position: relative;
  width: 97px;
  z-index: 19;
}
.image-3 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 97px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/181640/teddy-puppy.png)
    no-repeat center;
  background-size: cover;
  z-index: 20;
  border-radius: 10px;
}
.teddy {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  min-width: 0;
  height: 15px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 21;
}
.frame-4 {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 11px;
  position: relative;
  width: 97px;
  z-index: 22;
}
.group {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 97px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/181640/french-bulldog-puppy.png)
    no-repeat center;
  background-size: cover;
  z-index: 23;
  border-radius: 10px;
}
.french-bulldog {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  min-width: 0;
  height: 15px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 24;
}
.frame-5 {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 11px;
  position: relative;
  width: 97px;
  z-index: 25;
}
.image-div {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 97px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/181640/welsh-corgi-puppy.png)
    no-repeat center;
  background-size: cover;
  z-index: 26;
  border-radius: 10px;
}
.welsh-corgi-span {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  min-width: 0;
  height: 15px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 27;
}
.frame-div {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 11px;
  position: relative;
  width: 97px;
  z-index: 28;
}
.image-div-6 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 97px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/181640/teddy-puppy-alt.png)
    no-repeat center;
  background-size: cover;
  z-index: 29;
  border-radius: 10px;
}
.teddy-span {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  min-width: 0;
  height: 15px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 30;
}
.image-div-7 {
  position: relative;
  width: 334px;
  height: 334px;
  margin: 49px 0 0 30px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/181640/puppy-showcase-background.png)
    no-repeat center;
  background-size: cover;
  z-index: 31;
  border-radius: 40px;
}
.image-div-8 {
  position: absolute;
  width: 334px;
  height: 334px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-05/181640/puppy-showcase-foreground.png)
    no-repeat center;
  background-size: cover;
  z-index: 32;
  border-radius: 40px;
}
.rectangle-div {
  position: absolute;
  width: 115px;
  height: 47px;
  top: 29px;
  left: 36px;
  background: #d2c39c;
  z-index: 40;
}
.happy-moments-span {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 29px;
  top: 29px;
  left: 139px;
  color: #ffffff;
  font-family: AR DCCSTMoritaGB, var(--default-font-family);
  font-size: 21.79608917236328px;
  font-weight: 700;
  line-height: 28.749px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 41;
}
.rectangle {
  position: absolute;
  width: 82px;
  height: 47px;
  top: 38px;
  left: 178px;
  background: #d2c39c;
  z-index: 39;
}
.image-9 {
  position: relative;
  width: 334px;
  height: 334px;
  margin: 19px 0 0 30px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/181640/puppy-gallery-image.png)
    no-repeat center;
  background-size: cover;
  z-index: 33;
  overflow: visible auto;
  border-radius: 40px;
}
.flex-row-fb {
  position: relative;
  width: 222px;
  height: 99px;
  margin: 25px 0 0 90px;
  z-index: 42;
}
.rectangle-a {
  position: absolute;
  width: 82px;
  height: 52px;
  top: 0;
  left: 0;
  background: #a3d6b7;
  z-index: 34;
}
.text-content {
  display: flex;
  align-items: flex-start;
  justify-content: flex-end;
  position: absolute;
  width: 166px;
  height: 48px;
  top: 4px;
  left: 56px;
  color: #000000;
  font-family: AR DCCSTMoritaGB, var(--default-font-family);
  font-size: 18px;
  font-weight: 700;
  line-height: 23.742px;
  text-align: right;
  text-overflow: initial;
  text-transform: capitalize;
  z-index: 42;
  overflow: hidden;
}
.rectangle-b {
  position: absolute;
  width: 82px;
  height: 52px;
  top: 15px;
  left: 44px;
  background: #a3d6b7;
  z-index: 35;
}
.rectangle-c {
  position: absolute;
  width: 82px;
  height: 52px;
  top: 47px;
  left: 136px;
  background: #a3d6b7;
  z-index: 36;
}
.home-indicator {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 21px 0 0 100px;
  background: #000000;
  z-index: 38;
  border-radius: 100px;
}

.slider-container {
    position: relative;
    width: 100%;
    height: 550px; /* 设置一个固定高度 */
    margin-top: 20px;
    overflow-y: scroll; /* 启用垂直滚动 */
    scroll-snap-type: y mandatory; /* 可选：添加滚动吸附效果 */
    -webkit-overflow-scrolling: touch; /* 平滑滚动效果 */
    
    /* 隐藏滚动条 */
    scrollbar-width: none; /* Firefox */
    -ms-overflow-style: none; /* IE 和 Edge */
}
.slider-container::-webkit-scrollbar {
    display: none; /* Chrome, Safari 和 Opera */
}

</style>
  