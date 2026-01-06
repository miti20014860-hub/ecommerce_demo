// utils/formatTime.ts
import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';
import timezone from 'dayjs/plugin/timezone';
import utc from 'dayjs/plugin/utc';

dayjs.extend(relativeTime);
dayjs.extend(timezone);
dayjs.extend(utc);

dayjs.tz.setDefault('Asia/Hong_Kong');

import 'dayjs/locale/en';

dayjs.locale('en');

export const naturalTime = (dateString: string): string => {
  return dayjs.tz(dateString, 'Asia/Hong_Kong').fromNow();
};

export const formatDate = (dateString: string): string => {
  return dayjs.tz(dateString, 'Asia/Hong_Kong').format('MMMM D, YYYY');
};
