import CourseModel from "../models/coursesModel"

export const dashboardAnalytics=async (req,res)=>{
  const totalcourses= CourseModel.countDocuments({instituteId:req.user.id})
}